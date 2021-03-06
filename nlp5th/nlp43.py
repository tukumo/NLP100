#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list


if __name__ == '__main__':
    for chunks in chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            if chunk.dst != '-1':
                if '名詞' in {v.pos for v in chunk.morphs} and '動詞' in {v.pos for v in chunks[int(chunk.dst)].morphs}:
                    print('{0}\t{1}'.format(''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']),
                                            ''.join([morph.surface for morph in
                                                     chunks[int(chunk.dst)].morphs if morph.pos != '記号'])))
