#!/bin/bash
echo "Api Gateway"
lsof -i :5000 

echo "User management"
lsof -i :5001 

echo "Todo Management"
lsof -i :5002