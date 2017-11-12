// get_file.js
// issues a post request when a new file is to be added to the server

// Get File
var fileReader = new FileReader();
fileReader.onload = function() {
  var array_buffer = this.result;
  filename = files[0].name.toString();
  filename = filename.slice(0, -4);
}

fileReader.readAsArrayBuffer(files[0]);
var url = URL.createObjectURL(files[0]);

// XMLHttpRequest
var request = new XMLHttpRequest();

request.open('POST', url, true);
request.responseType = 'arraybuffer';

request.send(files[0]);
