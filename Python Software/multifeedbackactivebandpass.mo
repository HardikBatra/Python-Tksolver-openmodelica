model multifeedbackactivebandpass
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp annotation(
    Placement(visible = true, transformation(origin = {66, 2}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor r1(R = 10000)  annotation(
    Placement(visible = true, transformation(origin = {-56, 8}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor r3(R = 10000)  annotation(
    Placement(visible = true, transformation(origin = {-16, -40}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Capacitor c1(C = 6.8e-9)  annotation(
    Placement(visible = true, transformation(origin = {10, 8}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor c2(C = 1e-8)  annotation(
    Placement(visible = true, transformation(origin = {10, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor r2(R = 20000)  annotation(
    Placement(visible = true, transformation(origin = {44, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin annotation(
    Placement(visible = true, transformation(origin = {-16, 8}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {-40, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin1 annotation(
    Placement(visible = true, transformation(origin = {34, 8}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {8, 38}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-16, -86}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin2 annotation(
    Placement(visible = true, transformation(origin = {76, 34}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {52, 52}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 1, freqHz = 1930) annotation(
    Placement(visible = true, transformation(origin = {-84, -2}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
equation
  connect(r1.n, pin) annotation(
    Line(points = {{-46, 8}, {-16, 8}}, color = {0, 0, 255}));
  connect(c1.p, pin) annotation(
    Line(points = {{0, 8}, {-16, 8}}, color = {0, 0, 255}));
  connect(pin, r3.p) annotation(
    Line(points = {{-16, 8}, {-16, -30}}, color = {0, 0, 255}));
  connect(pin, c2.p) annotation(
    Line(points = {{-16, 8}, {-16, 46}, {0, 46}}, color = {0, 0, 255}));
  connect(c1.n, pin1) annotation(
    Line(points = {{20, 8}, {34, 8}}, color = {0, 0, 255}));
  connect(pin1, r2.p) annotation(
    Line(points = {{34, 8}, {34, 34}}, color = {0, 0, 255}));
  connect(pin1, opAmp.in_n) annotation(
    Line(points = {{34, 8}, {56, 8}}, color = {0, 0, 255}));
  connect(r3.n, ground1.p) annotation(
    Line(points = {{-16, -50}, {-16, -76}}, color = {0, 0, 255}));
  connect(c2.n, pin2) annotation(
    Line(points = {{20, 46}, {76, 46}, {76, 34}}, color = {0, 0, 255}));
  connect(r2.n, pin2) annotation(
    Line(points = {{54, 34}, {76, 34}}, color = {0, 0, 255}));
  connect(opAmp.out, pin2) annotation(
    Line(points = {{76, 2}, {76, 34}}, color = {0, 0, 255}));
  connect(opAmp.in_p, ground1.p) annotation(
    Line(points = {{56, -4}, {34, -4}, {34, -74}, {-16, -74}, {-16, -76}}, color = {0, 0, 255}));
  connect(sineVoltage.n, r1.p) annotation(
    Line(points = {{-84, 8}, {-66, 8}, {-66, 10}, {-66, 10}, {-66, 8}}, color = {0, 0, 255}));
  connect(sineVoltage.p, ground1.p) annotation(
    Line(points = {{-84, -12}, {-84, -12}, {-84, -76}, {-16, -76}, {-16, -76}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {-4, 81}, extent = {{-84, 23}, {84, -23}}, textString = "MULTIPLE FEEDBACK BAND PASS FILTER", textStyle = {TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic})}, coordinateSystem(initialScale = 0.1)));
end multifeedbackactivebandpass;
