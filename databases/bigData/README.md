Docker Commands

 `docker-compose up --build`


 Spark Commands - From the spark directory

 ```
    Compile
    -------
    sbt clean assembly
    sbt compile
    sbt package
    jar tvf target/scala-2.11/cse512-hotspot-analysis-template_2.11-0.1.0.jar 

    Hotcell Analysis
    ----------------
    spark-submit ./target/scala-2.11/CSE512-Hotspot-Analysis-Template-assembly-0.1.0.jar test/output hotcellanalysis src/resources/yellow_tripdata_2009-01_point.csv

    Hotzone Analysis
    ----------------
    spark-submit ./target/scala-2.11/CSE512-Hotspot-Analysis-Template-assembly-0.1.0.jar test/output hotzoneanalysis src/resources/point_hotzone.csv src/resources/zone-hotzone.csv 


    Output
    ------
    Files are written to the output directory - test/output


```