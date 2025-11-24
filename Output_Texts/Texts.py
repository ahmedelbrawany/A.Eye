

class Texts:
    def __init__(self):
        self.text = ""
    def get_object_text(self, img_shape, objects_detected, objects_center):
        self.text = ""
        # numOfObjects = 0
        string_right = ""
        string_cen = ""
        string_left = ""

        x_left = img_shape[1] / 4
        x_cen = x_left + x_left * 2

        if not objects_detected:
            self.text = ""
            return self.text
        print(objects_detected)
        for obj, x in zip(objects_detected, objects_center):
            if x > x_cen:
                string_right += f"{obj[0]} at distance {obj[1]} meters, "

            elif x > x_left:
                string_cen += f"{obj[0]} at distance {obj[1]} meters, "
            else:
                string_left += f"{obj[0]} at distance {obj[1]} meters, "

        if string_right:
            string_right += "on your right"

        if string_cen:
            if string_right:
                string_right += " ,and "
            string_cen += "front of you"

        if string_left:
            if string_cen:
                string_cen += " ,and "
            string_left += "on your left"

        self.text = "there is a " + string_right + string_cen + string_left
        return self.text