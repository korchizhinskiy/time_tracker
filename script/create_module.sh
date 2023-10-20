#!/bin/sh

MODULE_NAME=$1
MODULE_PATH=app/$1

if [[ $MODULE_NAME == "" ]]
then
  printf "Error!\nInput module name!\n"
  printf "Uses: ./bin/create_module.sh module_name\n"
  exit
fi

if [[ -d "$MODULE_PATH" ]]
then
  printf "Error!\nModule \`$MODULE_NAME\` already created!\n"
  exit
fi

# printf "1. Services\n2. Utils\n3. Tests\n4. Tasks\n"
# read -p "Введите пакеты, которые нужно создать (через запятую):\n" packages

fill_module() {
  mkdir -p $MODULE_PATH/models && touch $MODULE_PATH/models/__init__.py
  mkdir -p $MODULE_PATH/schemas && touch $MODULE_PATH/schemas/__init__.py
  mkdir -p $MODULE_PATH/tests && touch $MODULE_PATH/tests/__init__.py
  mkdir -p $MODULE_PATH/tasks && touch $MODULE_PATH/tasks/__init__.py
  mkdir -p $MODULE_PATH/services && touch $MODULE_PATH/services/__init__.py
  mkdir -p $MODULE_PATH/utils && touch $MODULE_PATH/utils/__init__.py
  
  touch $MODULE_PATH/config.py
  touch $MODULE_PATH/exceptions.py
  touch $MODULE_PATH/constants.py
  touch $MODULE_PATH/exceptions.py
  touch $MODULE_PATH/tasks.py
  touch $MODULE_PATH/router.py
  
  touch $MODULE_PATH/__init__.py
}

fill_module \
  && printf "Success!\nNew module has been created: \`$MODULE_PATH\`!" \
  || printf "Error!\nYou can see logs up this\n"
