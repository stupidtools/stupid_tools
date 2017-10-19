


def compare(orig, mod, begin_token, end_token):
    o = 0
    m = 0
    output = dict()
    while True:
        if o == len(orig):
            break
        if orig[o] == mod[m]:
            o += 1
            m += 1
            continue
        start_mod = m
        start_orig = o
        i = 0
        while True:
            if i == len(end_token):
                m += i
                break
            if mod[m + i] == end_token[i]:
                i += 1
                continue
            i = 0
            m += 1
        while True:
            if mod[m] != ' ':
                break
            m += 1
        end_mod = m
        end_phrase = mod[m:m+3]
        i = 0
        while True:
            if i == 3:
                end_orig = o
                break
            if orig[o + i] ==  end_phrase[i]:
                i += 1
                continue
            i = 0
            o += 1
        orig_phrase = orig[start_orig:end_orig].strip()
        mod_phrase = mod[start_mod:end_mod].strip().strip(begin_token).strip(end_token).strip()
        output[mod_phrase]= orig_phrase
    return output
        
        
        
            
                
    
    
