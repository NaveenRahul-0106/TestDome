class ChineseBox:
    count = 0
    def __init__(self, contained_box = None):
        self.contained_box = contained_box
        if (self.contained_box != None):
            ChineseBox.count +=1
            self.number_of_smaller_boxes()
        
    def number_of_smaller_boxes(self):
        return ChineseBox.count


if __name__ == "__main__":
    box = ChineseBox(ChineseBox())
    print(box.number_of_smaller_boxes())