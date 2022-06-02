const http = require("http");
const { exec } = require("child_process");

const port = 3000;

const server = http.createServer((req, res) => {
	res.setHeader("Access-Control-Allow-Origin", "*");
	switch (req.method) {
		case "GET":
			res.end("yee");	
			break;

		case "POST":
			let data = "";
			req.on("data", (chunk) => {
				data += chunk;
			});
			req.on("end", () => {
				console.log(data);
				res.end();
				console.log("starting python scritps");

				exec("python3 download.py " + data, (error, stdout, stderr) => {
					console.log(stdout);

					exec("python3 upload.py", (error, stdout, stderr) => {
						console.log(stdout);
					});
				});
			});
			break;
		
		default:
		res.statusCode = 405;
		res.end();
	}
});

server.listen(port, () => {
	console.log("Listening on port: " + port);
});
