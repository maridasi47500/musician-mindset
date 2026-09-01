
mkdir templates 
python3 scaffold.py computing_terms name
python3 scaffold.py musical_pieces title style composer score:staff key_signature time_signature pic
python3 scaffold.py musicalinstrument name
python3 scaffold.py profiles name f_or_m musicalinstrument_id:references hobbies_id:references
python3 scaffold.py profilehascomputingtermlogs computing_terms_id:references profiles_id:references content
python3 scaffold.py profilehasscorelogs musical_pieces_id:references profiles_id:references content
python3 scaffold.py hobbies name
