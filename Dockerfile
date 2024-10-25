FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64
ENV PATH $PATH:$JAVA_HOME/bin

USER airflow

# Remove conflicting packages and install specific versions
RUN pip uninstall -y apache-airflow apache-airflow-providers-apache-spark apache-airflow-providers-openlineage && \
    pip install --no-cache-dir \
    apache-airflow==2.7.1 \
    apache-airflow-providers-apache-spark>=4.1.0 \
    apache-airflow-providers-openlineage>=1.1.0 \
    pyspark==3.4.1

