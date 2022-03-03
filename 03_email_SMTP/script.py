#!/usr/bin/env python3

import json
import locale
import sys
import car_report, car_email


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"sales": 0}
  car_year_dict = {}
  max_car_sales = {}

  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    item_sales = item["total_sales"]
    if item_sales > max_sales["sales"]:
        max_sales["sales"] = item["total_sales"]
    else:
        max_car_sales = item
    # TODO: also handle most popular car_year
    car_year = item["car"]["car_year"]
    if car_year not in car_year_dict:
        # add new key to dict
        car_year_dict[car_year] = item["total_sales"]
    else:
        # append sales to year key
        car_year_dict[car_year] += item["total_sales"]
  car_year_sorted = sorted(car_year_dict.items(), key=lambda x: x[1], reverse=True)
  most_pop_year = next(iter(car_year_sorted))

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
        format_car(max_car_sales["car"]), max_sales["sales"]),
    "The most popular year was {} with {} sales.".format(
        most_pop_year[0], most_pop_year[1])
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  # TODO: turn this into a PDF report
  pdf_data = cars_dict_to_table(data)
  summary_html = '<br/>'.join(summary)
  by_sales_data = sorted(pdf_data[1:], key=lambda x: x[3], reverse=True)
  reports.generate('/tmp/cars.pdf', 'Car Sales', summary_html, pdf_data)
  # TODO: send the PDF report as an email attachment
  msg = emails.generate('automation@example.com', 
          'student-02-77407e6abc98@example.com',
          'Sales summary for last month',
          '\n'.join(summary),
          '/tmp/cars.pdf')
  emails.send(msg)


if __name__ == "__main__":
  main(sys.argv)
