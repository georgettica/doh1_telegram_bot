on_board_statuses = [u"בעמדה", u"מטבח", u"מחסן", u"האנגר", u"חדר מכונות", u"חמ",
                     u"מגורים", u"גשר", u"סיפון עליון", u"סע", u"סיפון תחתון", u"סת",
                     u"חדר בקרה", u"חב", u"חדר שרתים", u"חש", u"מרפאה"]
off_board_statuses = [u"מחלה", u"חופש", u"חול", u"מחוץ ליחידה בתפקיד", u"מלת",
                      u"מחוץ ליחידה אחר", u"מל", u"הפניה", u"קורס"]

for i in range(0, len(on_board_statuses)):
    on_board_statuses[i] = on_board_statuses[i][::-1]

for i in range(0, len(off_board_statuses)):
    off_board_statuses[i] = off_board_statuses[i][::-1]