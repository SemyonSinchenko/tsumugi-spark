// Inspired by https://github.com/apache/spark-connect-go/blob/master/cmd/spark-connect-example-spark-session/main.go

package main

import (
	"context"
	"flag"
	"log"

	"github.com/apache/spark-connect-go/v35/client/session"
	"github.com/apache/spark-connect-go/v35/client/sql"
)

var (
	remote = flag.String("remote", "sc://localhost:15002",
		"the remote address of Spark Connect server to connect to")
)

func main() {
	flag.Parse()
	ctx := context.Background()
	spark, err := session.NewSessionBuilder().Remote(*remote).Build(ctx)
	if err != nil {
		log.Fatalf("Failed: %s", err)
	}
	defer spark.Stop()

	df, err := spark.Sql(
		ctx,
		"select 1 as id, 'Thingy A' as productName, 'awesome thing.' as description, 'high' as priority, 0 as 'numViews'" +
			"union all"+
			"select 2 as id, 'Thingy B' as productName, 'availabele' as description, NULL as priority, 0 as numViews",
	)

	if err != nil {
		log.Fatalf("Failed: %s", err)
	}

	err = df.Show(ctx, 100, false)
	if err != nil {
		log.Fatalf("Failed: %s", err)
	}
}
