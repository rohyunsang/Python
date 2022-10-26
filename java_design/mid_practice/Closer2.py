def html_tag(tag):
    def wrap_text(msg):
        print(tag,' ',msg, ' ', tag)
    
    return wrap_text


print_h1 = html_tag('h1')
print_h1('첫 번째 해딩 타이틀')
del html_tag

print_h1('두 번째 해딩 타이틀') # wrap_text func에서 tag가 남아있음. 
