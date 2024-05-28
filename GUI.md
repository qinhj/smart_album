## Page 1: Home Page

## Page 2: Smart Album

### ui.load_pages

| QWidget | QBoxLayout |
| :------ | :--------- |
| page_2_top_widget | page_2_top_widget_layout |
| page_2_right_scrollAreaWidgetContents | scrollArea_layout_album |
| page_2_left_column_frame | album_list_layout |
| page_2_left_column.scrollAreaWidgetContents | page_2_left_column.scrollAreaLayout |

```txt
.------------------------------------------------------------------------------------------.
|                                     page_2_top_widget                                    |
|              (task label)                        (dir btn)             (task btn)        |
+---------------------------------------------+--------------------------------------------+
|       page_2_left_column_frame              |           page_2_right_scrollArea          |
|          (album_list_layout)                |                                            |
| .-----------------------------------------. | .----------------------------------------. |
| |        page_2_left_column               | | |  page_2_right_scrollAreaWidgetContents | |
| | /-------------------------------------\ | | |        (scrollArea_layout_album)       | |
| | |          title_label                | | | | .------------------------------------. | |
| | +-------------------------------------+ | | | |             PyImagePage            | | |
| | |         content_frame               | | | | | .--------------------------------. | | |
| | | .---------------------------------. | | | | | | PyImage                        | | | |
| | | |         scrollArea              | | | | | | | PyImage                        | | | |
| | | | .-----------------------------. | | | | | | | PyImage                        | | | |
| | | | |   scrollAreaWidgetContents  | | | | | | | | ...                            | | | |
| | | | |      (scrollAreaLayout)     | | | | | | | .--------------------------------. | | |
| | | | | .-------------------------. | | | | | | |                                    | | |
| | | | | | smart_album_list_widget | | | | | | | |                                    | | |
| | | | | | .---------------------. | | | | | | | |                                    | | |
| | | | | | | PyPushButton        | | | | | | | | |                                    | | |
| | | | | | | PyPushButton        | | | | | | | | |                                    | | |
| | | | | | | ....                | | | | | | | | |                                    | | |
| | | | | | | Stretch             | | | | | | | | |                                    | | |
| | | | | | | Spacing(10)         | | | | | | | | |                                    | | |
| | | | | | .---------------------. | | | | | | | |                                    | | |
| | | | | .-------------------------. | | | | | | |                                    | | |
| | | | .-----------------------------. | | | | | .------------------------------------. | |
| | | .---------------------------------. | | | |                                        | |
| | \-------------------------------------/ | | |                                        | |
| .-----------------------------------------. | .----------------------------------------. |
.---------------------------------------------+--------------------------------------------.
```

## Page 3: Face Cluster

### ui.load_pages

| QWidget | QBoxLayout |
| :------ | :--------- |
| page_3_top_widget | page_3_top_widget_layout |
| page_3_right_scrollAreaWidgetContents | scrollArea_layout_human |
| page_3_left_column_frame | human_list_layout |
| page_3_left_column.scrollAreaWidgetContents | page_3_left_column.scrollAreaLayout |

```txt
Similar as Page 2 Smart Album
```

## Page 4: Image Search

### ui.load_pages

| QWidget | QBoxLayout |
| :------ | :--------- |
| page_4_top_widget | page_4_top_widget_layout |
| page_4_search_info | search_info_layout |
| page_4_scrollAreaWidgetContents | scrollArea_layout_search |

```txt
.--------------------------------------------.
|             page_4_top_widget              |
| (task label) (dir btn) (img btn) (cmd btn) |
+--------------------------------------------|
| /----------------------------------------\ |
| |           page_4_search_info           | |
| | .------------------------------------. | |
| | |   _image_widget / _label_widget    | | |
| | .------------------------------------. | |
| +----------------------------------------+ |
| |            page_4_scrollArea           | |
| | .------------------------------------. | |
| | |   page_4_scrollAreaWidgetContents  | | |
| | |     (scrollArea_layout_search)     | | |
| | | .--------------------------------. | | |
| | | |           PyImagePage          | | | |
| | | | .----------------------------. | | | |
| | | | | PyImage                    | | | | |
| | | | | PyImage                    | | | | |
| | | | | ...                        | | | | |
| | | | .----------------------------. | | | |
| | | .--------------------------------. | | |
| | .------------------------------------. | |
| \----------------------------------------/ |
.--------------------------------------------.
```

## Page 5: Image Similarity

### ui.load_pages

| QWidget | QBoxLayout |
| :------ | :--------- |
| page_5_top_widget | page_5_top_widget_layout |
| page_5_scrollAreaWidgetContents | scrollArea_layout_similarity |

```txt
.--------------------------------------------.
|             page_5_top_widget              |
|   (task label)       (dir btn)  (cmd btn)  |
+--------------------------------------------+
|             page_5_scrollArea              |
| .----------------------------------------. |
| |     page_5_scrollAreaWidgetContents    | |
| |       (scrollArea_layout_search)       | |
| | .------------------------------------. | |
| | |             PyImagePage            | | |
| | | .--------------------------------. | | |
| | | | PyImage                        | | | |
| | | | PyImage                        | | | |
| | | | ...                            | | | |
| | | .--------------------------------. | | |
| | .------------------------------------. | |
| | |             PyImagePage            | | |
| | | .--------------------------------. | | |
| | | | PyImage                        | | | |
| | | | PyImage                        | | | |
| | | | ...                            | | | |
| | | .--------------------------------. | | |
| | .------------------------------------. | |
| | |                 ...                | | |
| | .------------------------------------. | |
| .----------------------------------------. |
+--------------------------------------------+
|            commit_delete_button            |
.--------------------------------------------.
