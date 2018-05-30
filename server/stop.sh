#!/bin/bash

pid=`ps | grep node | awk '{print $1}'`
echo $pid
kill -9 $pid
