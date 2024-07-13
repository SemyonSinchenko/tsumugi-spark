# TODO: This one should use variables instead of hardcoding
./sbin/start-connect-server.sh \
    --wait \
    --verbose \
    --jars tsumugi-server-1.0-SNAPSHOT.jar,protobuf-java-3.25.1.jar,deequ-2.0.7-spark-3.5.jar \
    --conf spark.connect.extensions.relation.classes=org.apache.spark.sql.DeequConnectPlugin \
    --packages org.apache.spark:spark-connect_2.12:3.5.1
