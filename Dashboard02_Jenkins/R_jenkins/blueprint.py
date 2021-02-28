from flask import Blueprint, render_template

jenkins_routes = Blueprint(
                "jenkins",
                 __name__,
                 url_prefix="/jenkins"
                 )

@jenkins_routes.route("")
def jenkins():
    return render_template("jenkins.html")
    
@jenkins_routes.route("/update/<string:job_name>")
def update(job_name):
    return render_template("jenkins_update.html")    

