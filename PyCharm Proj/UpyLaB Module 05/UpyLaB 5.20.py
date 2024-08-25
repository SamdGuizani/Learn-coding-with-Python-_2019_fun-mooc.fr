def replace(in_path, out_path, pattern, subst):
    with open(out_path, 'w', encoding='utf-8') as res:
        txt_init = open(in_path, encoding='utf-8')
        txt_init = txt_init.read()
        res.write(txt_init.replace(pattern, subst))
