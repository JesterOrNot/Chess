FROM gitpod/workspace-mysql
EXPOSE 3000
EXPOSE 3306
EXPOSE 5000
RUN bash -c "python3 new_db.py"
RUN bash -c "python3 db.py"
# Setup JAVA_HOME -- useful for docker commandline