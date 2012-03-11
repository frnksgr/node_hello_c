var ffi = require("node-ffi");

var libhello = new ffi.Library("./libhello", {
    "hello": [ "void", [] ],
    "hello_to": [ "void", ["string"]]
});

if (process.argv.length < 3) {
    console.log("calling hello() from libhello");
    libhello.hello();
} else {
    var msg = process.argv[2];
    console.log("calling hello_to(char*) from libhello with argument " + msg);
    libhello.hello_to(msg);
}


