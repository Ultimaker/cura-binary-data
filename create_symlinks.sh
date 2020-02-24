

ln -s -f $PWD/cura/resources/firmware ../Cura/resources

for dest in cura uranium; do
  for lang in $dest/resources/i18n/*;
  do
    link_loc=${lang/cura/Cura}
    link_loc=${link_loc/uranium/Uranium}
    for lang_file in $lang/*; do
      ln -s -f $PWD/$lang_file ../$link_loc
    done
  done
done
