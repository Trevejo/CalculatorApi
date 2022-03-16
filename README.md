# CalculatorApi
A advanced math calculator made with python using newton API

### How does it work?
It works by sending GET requests to newton API's website with a url-encoded math expression and your preferred operation and receive a JSON response with your problem solved.

### Available operations with examples
| Operation |    API Endpoint   |       Result      |
|:---------:|:-----------------:|:-----------------:|
| Simplify  | /simplify/2^2+2(2)| 8                 |
| Factor    | /factor/x^2 + 2x  | x (x + 2)         |
| Derive    | /derive/x^2+2x    | 2 x + 2           |
| Integrate | /integrate/x^2+2x | 1/3 x^3 + x^2 + C |
| Find 0's  | /zeroes/x^2+2x    | [-2, 0]           |
| Find Tangent| /tangent/2lx^3  | 12 x + -16        |
| Area Under Curve| /area/2:4lx^3| 60               |
| Cosine    | /cos/pi            | -1                 |
| Sine      | /sin/0            | 0                 |
| Tangent   | /tan/0            | 0                 |
| Inverse Cosine    | /arccos/1            | 0                 |
| Inverse Sine    | /arcsin/0            | 0                 |
| Inverse Tangent    | /arctan/0            | 0                 |
| Absolute Value    | /abs/-1            | 1                 |  
| Logarithm | /log/2l8           | 3               |

Keep in mind: To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.

To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.

To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).