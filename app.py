from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
   {
      'id':1,
      'title': 'Data Analyst',
      'location': 'Nairobi, Kenya',
      'salary': 'KES 500,000'
   },
   {
      'id':2,
      'title': 'Data Scientist',
      'location': 'Nairobi, Kenya',
      'salary': 'KES 700,000'
      },
   {
      'id':3,
      'title': 'Backend Engineer',
      'location': 'San Francisco',
      'salary': '$ 500,000'
   },
   {
      'id':4,
      'title': 'Frontend Engineer',
      'location': 'Remote',
      'salary': 'KES 600,000'
   }
    ]

@app.route('/')
def hello_world():
   return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
   return jsonify(JOBS)

if __name__=='__main__':
   app.run(host='0.0.0.0', debug=True)