var ffi = require("node-ffi");

var libhello = new ffi.Library("./libhello", {
    "hello": [ "void", [] ]
});

console.log("calling hello() from libhello");
libhello.hello();

