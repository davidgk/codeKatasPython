function replace_kata_name(){
   sed -i '' "s/blank/$1/g" project.sh;
   sed -i '' "s/blank/$1/g" test_example.py;
   uppercase_replacement=$(echo "$1" | tr '[:lower:]' '[:upper:]')
   sed -i '' "s/description/$uppercase_replacement/g" README.md;
}

