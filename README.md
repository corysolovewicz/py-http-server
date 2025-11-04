# Simple Python File Server

A minimal Python script to serve local files over HTTP — perfect for quick file sharing or testing across your host and virtual machines.

##Features
- Lightweight - under 10 lines of code  
- Auto-creates the target directory if missing  
- Works out-of-the-box with Python 3 (no dependencies)  
- Easy to access from other devices on the same network  

## How It Works
The script uses Python’s built-in [`http.server`](https://docs.python.org/3/library/http.server.html) module to spin up a simple HTTP server that lists and serves files from a specified directory.

## Directory Structure
```
your-repo/
├── file_server.py
├── files/            # Served files appear here
└── README.md
```

## Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/csolovewicz/py-http-server.git
   cd py-http-server
   ```

2. **Run the server**
   ```bash
   python3 file_server.py
   ```

3. **Access from a browser**
   ```
   http://localhost:8000
   ```
   or, if running inside a VM:
   ```
   http://<vm-ip-address>:8000
   ```

## Configuration
Inside `file_server.py`, you can modify:
```python
PORT, DIRECTORY = 8000, "files"
```
Change `PORT` for a different port or `DIRECTORY` to serve another folder.

## Stop the Server
Press **Ctrl + C** in the terminal.

## Example Use Cases
- Quickly share files between host and VM  
- Serve local static content for testing  
- Access exported reports or build artifacts remotely  

## License
 GPL 2.0
