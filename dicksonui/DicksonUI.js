function obey_forever() {
    var request = new XMLHttpRequest();
    request.open('get',window.location.href+ '/command');
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var child = document.createElement("script");
            child.setAttribute("id", "script");
            child.setAttribute("type", "text/javascript");
            child.innerHTML = this.responseText;
            document.body.replaceChild(child, document.getElementById("script"));
        }
    };
    request.onerror = function() {
        obey_forever();
    };
    request.send();
}

obey_forever();

function notify_server(event) {
    console.log('notifying server:', event);
    var request = new XMLHttpRequest();
    var data = {};
    for (x in event) {
        data[x] = event[x]
    }
    data.target = event.target.id;
    data.currentTarget = event.currentTarget.id;
    request.open('post', window.location.href+'/event');
    request.send(JSON.stringify(JSON.decycle(data), null, 4));
}

function notify_data(data) {
    console.log('notifying data:', data);
    var request = new XMLHttpRequest();
    request.open('post', window.location.href+'/data');
    request.send(JSON.stringify(JSON.decycle(data), null, 4));
}

if (typeof JSON.decycle !== 'function') {
    (function() {

        /**
         * Allows stringifing DOM elements.
         *
         * This is done in hope to identify the node when dumping.
         *
         * @param {Element} node DOM Node (works best for DOM Elements).
         * @returns {String}
         */
        function stringifyNode(node) {
            var text = "";
            switch (node.nodeType) {
                case node.ELEMENT_NODE:
                    text = node.nodeName.toLowerCase();
                    if (node.id.length) {
                        text += '#' + node.id;
                    } else {
                        if (node.className.length) {
                            text += '.' + node.className.replace(/ /, '.');
                        }
                        if ('textContent' in node) {
                            text += '{textContent:' +
                                (node.textContent.length < 20 ? node.textContent : node.textContent.substr(0, 20) + '...') +
                                '}';
                        }
                    }
                    break;
                    // info on values: http://www.w3.org/TR/DOM-Level-2-Core/core.html#ID-1841493061
                default:
                    text = node.nodeName;
                    if (node.nodeValue !== null) {
                        text += '{value:' +
                            (node.nodeValue.length < 20 ? node.nodeValue : node.nodeValue.substr(0, 20) + '...') +
                            '}';
                    }
                    break;
            }
            return text;
        }

        JSON.decycle = function decycle(object, stringifyNodes) {
            'use strict';

            // Make a deep copy of an object or array, assuring that there is at most
            // one instance of each object or array in the resulting structure. The
            // duplicate references (which might be forming cycles) are replaced with
            // an object of the form
            //      {$ref: PATH}
            // where the PATH is a JSONPath string that locates the first occurance.
            // So,
            //      var a = [];
            //      a[0] = a;
            //      return JSON.stringify(JSON.decycle(a));
            // produces the string '[{"$ref":"$"}]'.

            // NOTE! If your object contains DOM Nodes you might want to use `stringifyNodes` option
            // This will dump e.g. `div` with id="some-id" to string: `div#some-id`.
            // You will avoid some problems, but you won't to be able to fully retro-cycle.
            // To dump almost any variable use: `alert(JSON.stringify(JSON.decycle(variable, true)));`

            // JSONPath is used to locate the unique object. $ indicates the top level of
            // the object or array. [NUMBER] or [STRING] indicates a child member or
            // property.

            var objects = [], // Keep a reference to each unique object or array
                stringifyNodes = typeof(stringifyNodes) === 'undefined' ? false : stringifyNodes,
                paths = []; // Keep the path to each unique object or array

            return (function derez(value, path) {

                // The derez recurses through the object, producing the deep copy.

                var i, // The loop counter
                    name, // Property name
                    nu; // The new object or array

                // if we have a DOM Element/Node convert it to textual info.

                if (stringifyNodes && typeof value === 'object' && value !== null && 'nodeType' in value) {
                    return stringifyNode(value);
                }

                // typeof null === 'object', so go on if this value is really an object but not
                // one of the weird builtin objects.

                if (typeof value === 'object' && value !== null &&
                    !(value instanceof Boolean) &&
                    !(value instanceof Date) &&
                    !(value instanceof Number) &&
                    !(value instanceof RegExp) &&
                    !(value instanceof String)) {

                    // If the value is an object or array, look to see if we have already
                    // encountered it. If so, return a $ref/path object. This is a hard way,
                    // linear search that will get slower as the number of unique objects grows.

                    for (i = 0; i < objects.length; i += 1) {
                        if (objects[i] === value) {
                            return {
                                $ref: paths[i]
                            };
                        }
                    }

                    // Otherwise, accumulate the unique value and its path.

                    objects.push(value);
                    paths.push(path);

                    // If it is an array, replicate the array.

                    if (Object.prototype.toString.apply(value) === '[object Array]') {
                        nu = [];
                        for (i = 0; i < value.length; i += 1) {
                            nu[i] = derez(value[i], path + '[' + i + ']');
                        }
                    } else {

                        // If it is an object, replicate the object.

                        nu = {};
                        for (name in value) {
                            if (Object.prototype.hasOwnProperty.call(value, name)) {
                                nu[name] = derez(value[name],
                                    path + '[' + JSON.stringify(name) + ']');
                            }
                        }
                    }
                    return nu;
                }
                return value;
            }(object, '$'));
        };
    })();
}


if (typeof JSON.retrocycle !== 'function') {
    JSON.retrocycle = function retrocycle($) {
        'use strict';

        // Restore an object that was reduced by decycle. Members whose values are
        // objects of the form
        //      {$ref: PATH}
        // are replaced with references to the value found by the PATH. This will
        // restore cycles. The object will be mutated.

        // The eval function is used to locate the values described by a PATH. The
        // root object is kept in a $ variable. A regular expression is used to
        // assure that the PATH is extremely well formed. The regexp contains nested
        // * quantifiers. That has been known to have extremely bad performance
        // problems on some browsers for very long strings. A PATH is expected to be
        // reasonably short. A PATH is allowed to belong to a very restricted subset of
        // Goessner's JSONPath.

        // So,
        //      var s = '[{"$ref":"$"}]';
        //      return JSON.retrocycle(JSON.parse(s));
        // produces an array containing a single element which is the array itself.

        var px =
            /^\$(?:\[(?:\d+|\"(?:[^\\\"\u0000-\u001f]|\\([\\\"\/bfnrt]|u[0-9a-zA-Z]{4}))*\")\])*$/;

        (function rez(value) {

            // The rez function walks recursively through the object looking for $ref
            // properties. When it finds one that has a value that is a path, then it
            // replaces the $ref object with a reference to the value that is found by
            // the path.

            var i, item, name, path;

            if (value && typeof value === 'object') {
                if (Object.prototype.toString.apply(value) === '[object Array]') {
                    for (i = 0; i < value.length; i += 1) {
                        item = value[i];
                        if (item && typeof item === 'object') {
                            path = item.$ref;
                            if (typeof path === 'string' && px.test(path)) {
                                value[i] = eval(path);
                            } else {
                                rez(item);
                            }
                        }
                    }
                } else {
                    for (name in value) {
                        if (typeof value[name] === 'object') {
                            item = value[name];
                            if (item) {
                                path = item.$ref;
                                if (typeof path === 'string' && px.test(path)) {
                                    value[name] = eval(path);
                                } else {
                                    rez(item);
                                }
                            }
                        }
                    }
                }
            }
        }($));
        return $;
    };
}
