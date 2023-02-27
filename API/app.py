import math
import os

import georasters as gr
import rasterio
from flask import Flask, jsonify
from flask import request
from osgeo import gdal
import pandas as pd
import uuid

import GeoTiff as gt

app = Flask(__name__)


@app.route('/')
def index():
    print(request.values)
    upper_left_x = float(request.values.get('ux', 0))
    upper_left_y = float(request.values.get('uy', 0))
    lower_right_x = float(request.values.get('lx', 0))
    lower_right_y = float(request.values.get('ly', 0))
    x1 = math.ceil(abs(upper_left_x))
    y1 = math.ceil(abs(upper_left_y))
    x2 = math.ceil(abs(lower_right_x))
    y2 = math.ceil(abs(lower_right_y))

    print(x1, y1, x2, y2)

    # look up for image files containing the coordinate points
    file1 = gt.lookUpForImageFile(upper_left_x, upper_left_y, gt.determine_x_position(upper_left_x),
                                  gt.determine_y_position(upper_left_y))
    file2 = gt.lookUpForImageFile(lower_right_x, lower_right_y, gt.determine_x_position(lower_right_x),
                                  gt.determine_y_position(lower_right_y))
    window = (upper_left_x, upper_left_y, lower_right_x, lower_right_y)

    # if both the points lie in the same image file then use the looked up file to
    # get the heights and store it in a data frame
    if file1 == file2:
        cropped_file_name = str(uuid.uuid4()) + '.tif'
        gdal.Translate(cropped_file_name, file1, projWin=window)
        img4 = rasterio.open(cropped_file_name)
        full_img4 = img4.read()
        df = pd.DataFrame(full_img4[0])
        img4.close()
        os.remove(cropped_file_name)
        # df4.to_csv('croppedYo1.csv', index=False, header=False)

    # if both the points lie in two image files adjacent to each other
    # than merge both the looked up files to get the heights and store it in a data frame
    elif (x1 == x2 and y1 == y2 + 1) or (x1 == x2 + 1 and y1 == y2):
        files_to_mosaic = [file1, file2]
        merged_file_name = str(uuid.uuid4()) + '.tif'
        g = gdal.Warp(merged_file_name, files_to_mosaic, format="GTiff")
        g = None
        cropped_file_name = str(uuid.uuid4()) + '.tif'
        gdal.Translate(cropped_file_name, merged_file_name, projWin=window)
        img41 = rasterio.open(cropped_file_name)
        full_img41 = img41.read()
        df = pd.DataFrame(full_img41[0])
        img41.close()
        os.remove(merged_file_name)
        os.remove(cropped_file_name)
        # df41.to_csv('heights_dataset.csv', index=False, header=False)

    # if both the points lie in two image files placed diagonal to each other
    # than merge 4 image files containing the requested terrain region to get
    # the heights and store it in a data frame
    elif (x1 == x2 + 1 and y1 == y2 + 1):
        file3 = gt.lookUpForImageFile(lower_right_x, upper_left_y, gt.determine_x_position(lower_right_x),
                                      gt.determine_y_position(upper_left_y))
        file4 = gt.lookUpForImageFile(upper_left_x, lower_right_y, gt.determine_x_position(upper_left_x),
                                      gt.determine_y_position(lower_right_y))
        print(file3)
        print(file4)
        merged_file_name = str(uuid.uuid4()) + '.tif'
        files_to_mosaic = [file1, file2, file3, file4]
        g = gdal.Warp(merged_file_name, files_to_mosaic, format="GTiff")
        g = None
        cropped_file_name = str(uuid.uuid4()) + '.tif'
        gdal.Translate(cropped_file_name, merged_file_name, projWin=window)
        img42 = rasterio.open(cropped_file_name)
        full_img42 = img42.read()
        df = pd.DataFrame(full_img42[0])
        img42.close()
        os.remove(merged_file_name)
        os.remove(cropped_file_name)

    # convert the data frame into a json format
    json_data = df.to_json(orient='values')
    print(json_data)

    return jsonify(json_data)


@app.route('/ougs/')
def ougs():
    print(request.values)
    upper_left_x = float(request.values.get('ux', 0))
    upper_left_y = float(request.values.get('uy', 0))
    lower_right_x = float(request.values.get('lx', 0))
    lower_right_y = float(request.values.get('ly', 0))
    x1 = math.ceil(abs(upper_left_x))
    y1 = math.ceil(abs(upper_left_y))
    x2 = math.ceil(abs(lower_right_x))
    y2 = math.ceil(abs(lower_right_y))

    print(x1, y1, x2, y2)

    # look up for image files containing the coordinate points
    file1 = gt.lookUpForImageFile(upper_left_x, upper_left_y, gt.determine_x_position(upper_left_x),
                                  gt.determine_y_position(upper_left_y))
    file2 = gt.lookUpForImageFile(lower_right_x, lower_right_y, gt.determine_x_position(lower_right_x),
                                  gt.determine_y_position(lower_right_y))
    window = (upper_left_x, upper_left_y, lower_right_x, lower_right_y)

    # if both the points lie in the same image file then use the looked up file to
    # get the heights and store it in a data frame
    if file1 == file2:
        cropped_file_name = str(uuid.uuid4()) + '.tif'
        gdal.Translate(cropped_file_name, file1, projWin=window)
        cropped = gr.from_file(cropped_file_name)
        df = cropped.to_pandas()
        df1 = modifydf_ougs(df)

    # if both the points lie in two image files adjacent to each other
    # than merge both the looked up files to get the heights and store it in a data frame
    elif (x1 == x2 and y1 == y2 + 1) or (x1 == x2 + 1 and y1 == y2):
        files_to_mosaic = [file1, file2]
        merged_file_name = str(uuid.uuid4()) + '.tif'
        g = gdal.Warp(merged_file_name, files_to_mosaic, format="GTiff")
        g = None
        cropped_file_name = str(uuid.uuid4()) + '.tif'
        gdal.Translate(cropped_file_name, merged_file_name, projWin=window)
        cropped = gr.from_file(cropped_file_name)
        df = cropped.to_pandas()
        df1 = modifydf_ougs(df)
        os.remove(merged_file_name)

    # if both the points lie in two image files placed diagonal to each other
    # than merge 4 image files containing the requested terrain region to get
    # the heights and store it in a data frame
    elif (x1 == x2 + 1 and y1 == y2 + 1):
        file3 = gt.lookUpForImageFile(lower_right_x, upper_left_y, gt.determine_x_position(lower_right_x),
                                      gt.determine_y_position(upper_left_y))
        file4 = gt.lookUpForImageFile(upper_left_x, lower_right_y, gt.determine_x_position(upper_left_x),
                                      gt.determine_y_position(lower_right_y))
        print(file3)
        print(file4)
        merged_file_name = str(uuid.uuid4()) + '.tif'
        files_to_mosaic = [file1, file2, file3, file4]
        g = gdal.Warp(merged_file_name, files_to_mosaic, format="GTiff")
        g = None
        cropped_file_name = str(uuid.uuid4()) + '.tif'
        gdal.Translate(cropped_file_name, merged_file_name, projWin=window)
        cropped = gr.from_file(cropped_file_name)
        df = cropped.to_pandas()
        df1 = modifydf_ougs(df)
        os.remove(merged_file_name)

    # convert the data frame into a json format
    json_data1 = df1.to_json(orient='values')
    print(json_data1)

    return jsonify(json_data1)


def modifydf_ougs(df):
    lst = df.iloc[-1].tolist()
    row = int(lst[0]) + 1
    col = int(lst[1]) + 1
    df.loc[:, "row"] = df["row"].apply(lambda x: (x * 32.8084))
    df.loc[:, "col"] = df["col"].apply(lambda x: (x * 32.8084))
    minimum = df["value"].min()
    print(minimum)
    df.loc[:, "value"] = df["value"].apply(lambda x: (x-minimum) * 10)
    df = df.drop(['x', 'y'], axis=1)
    df = df.iloc[:, [1, 0, 2]]
    df2 = df.rename({'col': 'x', 'row': 'y'}, axis=1)
    df1 = pd.DataFrame({"x": [col], "y": [row]})
    df1 = pd.concat([df1, df2])
    df1 = df1.round(2)
    return df1


if __name__ == "__main__":
    app.run(debug=True)
