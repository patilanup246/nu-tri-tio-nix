import requests
import json
import csv


def main():
    names = ["Sweetgreen", "Pret A Manger US", "Panda Express", "Nanoosh", "Yard House", "Muscle Maker Grill",
             "Hummus And Pita Co.", "Pinkberry", "Mrs. Fields", "Fields Good Chicken", "The Little Beet",
             "Cheesecake Factory", "GRK Fresh Greek", "Wagamama", "Red Mango", "Chipotle", "Domino's", "Starbucks",
             "Five Guys", "Shake Shack", "Tender Greens"]
    output_file = 'result_nutritionix.csv'
    data_to_file = open(output_file, 'w', newline='')
    csv_writer = csv.writer(data_to_file, delimiter=",")
    csv_writer.writerow(
        ["Restaurant", "Food Item", "Serving Size", "Calories", "Calories from Fat", "Total Fat", "Saturated Fat",
         "Trans Fat", "Cholesterol", "Sodium", "Total Carbohydrates", "Dietary Fiber", "Sugars", "Proteins",
         "Vitamin A", "Vitamin C", "Calcium", "Iron"
         ])
    url = "https://d1gvlspmcma3iu.cloudfront.net/brands-restaurant.json.gz"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    numberrecords = 0
    for item in names:
        for _data in parsed:
            if _data['name'] == item:
                urlbrand = "https://www.nutritionix.com/nixapi/brands/" + _data['id'] + "/items/1?limit=2000&search="
                responsebrand = requests.get(urlbrand)
                databrand = responsebrand.text
                parsedbrand = json.loads(databrand)
                for _databrand in parsedbrand["items"]:
                    try:
                        numberrecords += 1
                        print(str(numberrecords) + " ]Brand: " + _data["name"] + ", Food :" + _databrand["item_name"])
                        urlfood = "https://www.nutritionix.com/nixapi/items/" + _databrand["item_id"]
                        responsefood = requests.get(urlfood)
                        datafood = responsefood.text
                        parsedfood = json.loads(datafood)

                        Restaurant = '"'+ _data['name'] +'"'
                        Food_Item = '"'+ parsedfood['item_name'] +'"'
                        Serving_Size = str(parsedfood['serving_qty']) +" "+ str(parsedfood['serving_unit'])
                        if parsedfood['metric_qty']!="":
                            Serving_Size ='"'+ Serving_Size + " ( "+ str(parsedfood['metric_qty'] )+" "+ str(parsedfood['metric_unit']) +" )" +'"'

                        Calories = parsedfood['calories']
                        Calories_from_Fat = int(parsedfood['total_fat']) * 9
                        Total_Fat = parsedfood['total_fat']
                        Saturated_Fat = parsedfood['saturated_fat']
                        Trans_Fat = parsedfood['trans_fat']
                        Cholesterol = parsedfood['cholesterol']
                        Sodium = parsedfood['sodium']
                        Total_Carbohydrates = parsedfood['total_carb']
                        Dietary_Fiber = parsedfood['dietary_fiber']
                        Sugars = parsedfood['sugars']
                        Proteins = parsedfood['protein']
                        Vitamin_A = parsedfood['vitamin_a']
                        Vitamin_C = parsedfood['vitamin_c']
                        Calcium = parsedfood['calcium_dv']
                        Iron = parsedfood['iron_dv']

                        csv_writer.writerow(
                            [Restaurant, Food_Item, Serving_Size, Calories, Calories_from_Fat, Total_Fat, Saturated_Fat,
                             Trans_Fat, Cholesterol, Sodium, Total_Carbohydrates, Dietary_Fiber, Sugars, Proteins,
                             Vitamin_A, Vitamin_C, Calcium, Iron])
                    except Exception:
                        pass  # or you could use 'continue'
    data_to_file.close()


if __name__ == '__main__':
    main()
