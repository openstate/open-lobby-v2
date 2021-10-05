#!/bin/bash

cd /opt/app
for i in `ls -1 /opt/app/libraries/svelte-oddk/packages/`;
do
  echo $i
  yarn add "file:/opt/app/libraries/svelte-oddk/packages/$i/"
done
