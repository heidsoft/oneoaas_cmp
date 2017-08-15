#!/bin/bash

#定义应用根目录
APP_ROOT=$(dirname "${BASH_SOURCE}")/..

echo ${APP_ROOT}

cd ${APP_ROOT}

rm -rf home_application/*.py
rm -rf home_application/aliyun/*.py
rm -rf home_application/aws/*.py
rm -rf home_application/migrations/*.py
rm -rf home_application/overview/*.py
rm -rf home_application/qcloud/*.py
rm -rf home_application/ucloud/*.py
rm -rf home_application/vmware/*.py
rm -rf hybirdsdk/*.py
rm -rf hybirdsdk/*.py



