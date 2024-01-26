#!/bin/bash
#
curl -s -L -X HEAD -W "%{http_code}" "$1"
