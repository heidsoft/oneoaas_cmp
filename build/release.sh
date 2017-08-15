#!/bin/bash

echo "release start ..."

#定义应用根目录
APP_NAME="oneoaas-cmp"
APP_PKG=${APP_NAME}.tar.gz
APP_ROOT=$(dirname "${BASH_SOURCE}")/..
RELEASE_ROOT=release/oneoaas-cmp
APP_PUBLIC_DIR="account app_control blueking common conf error_pages home_application hybirdsdk  QcloudApi static templates wssh"
APP_PUBLIC_FILE="__init__.py manage.py requirements.txt settings.py urls.py wsgi.py"
cd ${APP_ROOT}


echo "delete some py file "

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

echo "create release dir "

mkdir -p ${RELEASE_ROOT}
mkdir -p ${RELEASE_ROOT}/src

cp -rf APP_PUBLIC_DIR ${RELEASE_ROOT}/src

cp -rf APP_PUBLIC_FILE ${RELEASE_ROOT}/src

cp -rf app.yml ${RELEASE_ROOT}/src

cp -rf pkgs ${RELEASE_ROOT}

tar zcf ${APP_PKG}  ${RELEASE_ROOT}

echo "release finish ..."


