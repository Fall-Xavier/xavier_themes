## Description
This library is used to create panels on the terminal. Besides that, it can also create beautiful colorful text or make something that is still related to the 2 above.

## Example
```python
from xavier.panel import Panel

Panel("aku sayang kamu")
```
You can add parameters : widht, colorpanel, colortext

```python
from xavier.panel import Panel

Panel("aku sayang kamu",widht=50,colorpanel="GREEN",colortext="BLUE")
```
You can create a panel that adjusts the size of the text by adding : widht="FIT" or widht="fit"
```python
from xavier.panel import Panel

Panel("aku sayang kamu",widht="FIT")
```


## Valid Color List
```
• RED
• GREEN
• YELLOW
• BLUE
• ORANGE
• CYAN
• WHITE
• BLACK
• DEFAULT/NO_COLOR
```

## Special Thanks For
```
- Dapunta Khurayra
- Angga Kurniawan
- Latip Harkat
- Nanta XE
- Rizky Dev
- ExtremeBoy
```

## License
Use MIT License (MIT). Please see [License File](https://github.com/Fall-Xavier/xavier/blob/main/LICENSE) for more information license.
