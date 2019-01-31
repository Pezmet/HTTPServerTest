from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson
import re

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write ("HTTP Test Server \n")
        self.wfile.write (' \n')
        # Print pipelines
        self.wfile.write ('Pipeline Status: \n')                
        self.wfile.write ('Pipeline Restarts: ')
        self.wfile.write (nr_pipe_restarting)
        self.wfile.write (' \n')
        self.wfile.write ('Pipeline Sucesses: ')
        self.wfile.write (nr_pipe_success)
        self.wfile.write (' \n')
        self.wfile.write ('Pipeline Canceled: ')
        self.wfile.write (nr_pipe_canceled)
        self.wfile.write (' \n')
        self.wfile.write ('Pipeline Killed: ')
        self.wfile.write (nr_pipe_killed)
        self.wfile.write (' \n')
        self.wfile.write ('Pipeline Error: ')
        self.wfile.write (nr_pipe_error)
        self.wfile.write (' \n')
        self.wfile.write (' \n')
        # Print jobs
        self.wfile.write ('Jobs Status: \n')
        self.wfile.write ('Job Restarts: ')
        self.wfile.write (nr_job_restarting)
        self.wfile.write (' \n')
        self.wfile.write ('Job Sucesses: ')
        self.wfile.write (nr_job_success)
        self.wfile.write (' \n')
        self.wfile.write ('Jobs Canceled: ')
        self.wfile.write (nr_job_canceled)
        self.wfile.write (' \n')
        self.wfile.write ('Jobs Killed: ')
        self.wfile.write (nr_job_killed)
        self.wfile.write (' \n')
        self.wfile.write ('Job Errors: ')
        self.wfile.write (nr_job_error)
        self.wfile.write (' \n')       
        self.wfile.write (' ')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        self.end_headers()
        
    def do_POST(self):
        global nr_pipe_canceled, nr_pipe_restarting, nr_pipe_killed, nr_pipe_success, nr_pipe_error, nr_job_canceled, nr_job_restarting, nr_job_killed, nr_job_success, nr_job_error
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        # ! Stirng to dictionary for output ?
        data = simplejson.loads(self.data_string)
        print "{}".format(data)
        # Pipeline counter
        if data['event'] == 'cerebro.pipeline.canceled':
            nr_pipe_canceled += 1
        if data['event'] == 'cerebro.pipeline.restarting':
            nr_pipe_restarting += 1
        if data['event'] == 'cerebro.pipeline.killed':
            nr_pipe_killed += 1
        if data['event'] == 'cerebro.pipeline.success':
            nr_pipe_success += 1
        if data['event'] == 'cerebro.pipeline.error':
            nr_pipe_error += 1
        # Jobs counter    
        if data['event'] == 'cerebro.job.canceled':
            nr_job_canceled += 1
        if data['event'] == 'cerebro.job.restarting':
            nr_job_restarting += 1
        if data['event'] == 'cerebro.job.killed':
            nr_job_killed += 1
        if data['event'] == 'cerebro.job.success':
            nr_job_success += 1
        if data['event'] == 'cerebro.job.error':
            nr_job_error += 1            
        self.end_headers()
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Started HTTP Test Server@localhost:80'
    httpd.serve_forever()

#Will need refactor
global nr_pipe_canceled, nr_pipe_restart, nr_pipe_killed, nr_pipe_success, nr_pipe_error, nr_job_canceled, nr_job_restarting, nr_job_killed, nr_job_success, nr_job_error
nr_pipe_canceled = 0
nr_pipe_restarting = 0
nr_pipe_killed = 0
nr_pipe_success = 0
nr_pipe_error = 0
nr_job_canceled = 0
nr_job_restarting = 0
nr_job_killed = 0
nr_job_success = 0
nr_job_error = 0

if __name__ == "__main__":
    from sys import argv
        
    if len(argv) == 2:
        run(port=int(argv[1]))

    else:
        run()


