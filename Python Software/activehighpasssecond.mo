model activehighpasssecond
  Modelica.Electrical.Analog.Basic.Capacitor c1 annotation(
    Placement(visible = true, transformation(origin = {-68, 24}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Capacitor c2 annotation(
    Placement(visible = true, transformation(origin = {-12, 24}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor r4 annotation(
    Placement(visible = true, transformation(origin = {22, 52}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin1 annotation(
    Placement(visible = true, transformation(origin = {94, 22}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {64, 52}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor resistor1 annotation(
    Placement(visible = true, transformation(origin = {64, -8}, extent = {{10, -10}, {-10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor resistor2 annotation(
    Placement(visible = true, transformation(origin = {34, -34}, extent = {{10, -10}, {-10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Interfaces.Pin pin2 annotation(
    Placement(visible = true, transformation(origin = {34, -8}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {22, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Resistor r3 annotation(
    Placement(visible = true, transformation(origin = {16, -26}, extent = {{-12, -12}, {12, 12}}, rotation = -90)));
  Modelica.Electrical.Analog.Interfaces.Pin pin3 annotation(
    Placement(visible = true, transformation(origin = {16, 24}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {18, 56}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {26, -86}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 1, freqHz = 1)  annotation(
    Placement(visible = true, transformation(origin = {-90, -14}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Ground ground1 annotation(
    Placement(visible = true, transformation(origin = {-90, -62}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Interfaces.Pin pin annotation(
    Placement(visible = true, transformation(origin = {-42, 24}, extent = {{-6, -6}, {6, 6}}, rotation = 0), iconTransformation(origin = {-14, 54}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Ideal.IdealOpAmp3Pin opAmp annotation(
    Placement(visible = true, transformation(origin = {48, 22}, extent = {{-10, 10}, {10, -10}}, rotation = 0)));
equation
  connect(sineVoltage.n, ground1.p) annotation(
    Line(points = {{-90, -24}, {-90, -52}}, color = {0, 0, 255}));
  connect(sineVoltage.p, c1.n) annotation(
    Line(points = {{-90, -4}, {-90, 24}, {-78, 24}}, color = {0, 0, 255}));
  connect(c1.p, pin) annotation(
    Line(points = {{-58, 24}, {-42, 24}}, color = {0, 0, 255}));
  connect(pin, c2.n) annotation(
    Line(points = {{-42, 24}, {-22, 24}}, color = {0, 0, 255}));
  connect(c2.p, pin3) annotation(
    Line(points = {{-2, 24}, {14, 24}, {14, 24}, {16, 24}}, color = {0, 0, 255}));
  connect(pin2, resistor2.n) annotation(
    Line(points = {{34, -8}, {34, -24}}, color = {0, 0, 255}));
  connect(resistor2.p, ground.p) annotation(
    Line(points = {{34, -44}, {34, -44}, {34, -76}, {26, -76}, {26, -76}}, color = {0, 0, 255}));
  connect(pin3, r3.p) annotation(
    Line(points = {{16, 24}, {16, -14}}, color = {0, 0, 255}));
  connect(r3.n, ground.p) annotation(
    Line(points = {{16, -38}, {16, -76}, {26, -76}}, color = {0, 0, 255}));
  connect(pin2, resistor1.n) annotation(
    Line(points = {{34, -8}, {54, -8}}, color = {0, 0, 255}));
  connect(resistor1.p, pin1) annotation(
    Line(points = {{74, -8}, {74, -8}, {74, 22}, {94, 22}, {94, 22}}, color = {0, 0, 255}));
  connect(r4.p, pin1) annotation(
    Line(points = {{32, 52}, {74, 52}, {74, 22}, {94, 22}}, color = {0, 0, 255}));
  connect(r4.n, pin) annotation(
    Line(points = {{12, 52}, {-42, 52}, {-42, 24}}, color = {0, 0, 255}));
  connect(pin3, opAmp.in_p) annotation(
    Line(points = {{16, 24}, {38, 24}, {38, 28}}, color = {0, 0, 255}));
  connect(pin2, opAmp.in_n) annotation(
    Line(points = {{34, -8}, {34, 16}, {38, 16}}, color = {0, 0, 255}));
  connect(opAmp.out, pin1) annotation(
    Line(points = {{58, 22}, {94, 22}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {1, 84}, extent = {{-83, 12}, {83, -12}}, textString = "ACTIVE HIGH PASS FILTER SECOND ORDER", textStyle = {TextStyle.Italic, TextStyle.Italic})}, coordinateSystem(initialScale = 0.1)));
end activehighpasssecond;
