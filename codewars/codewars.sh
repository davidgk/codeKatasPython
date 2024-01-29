function replace_kata_name(){
   sed -i '' "s/blank/$1/g" project.sh;
   sed -i '' "s/blank/$1/g" test_example.py;
}

