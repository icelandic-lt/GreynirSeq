from greynirseq.ner import aligner, postagger


def test_add_mark(ner_tagged_sentences_en, ner_tagged_sentences_is, ner_final_simple):
    parser = aligner.NERParser(ner_tagged_sentences_en, ner_tagged_sentences_is)
    for i, (en_parse, is_parse, pair_info) in enumerate(parser.parse_files_gen(None)):
        en_tokens = en_parse.sent.split()
        is_tokens = is_parse.sent.split()
        for idx, alignment in enumerate(pair_info.pair_map):
            en_ner_marker, is_ner_marker, distance = alignment.marker_1, alignment.marker_2, alignment.distance
            en_ner_marker = postagger.NERPoSMarker.from_NERMarker(en_ner_marker)
            en_ner_marker.pos_tag = "x"
            is_ner_marker = postagger.NERPoSMarker.from_NERMarker(is_ner_marker)
            is_ner_marker.pos_tag = "x"
            # The distance should be small
            assert distance < 0.3
            postagger.add_marker(en_ner_marker, en_tokens, idx, enumerate_marker=True, add_pos_tag=True)
            postagger.add_marker(is_ner_marker, is_tokens, idx, enumerate_marker=True, add_pos_tag=True)
        assert " ".join(en_tokens) == ner_final_simple[i][0]
        assert " ".join(is_tokens) == ner_final_simple[i][1]
