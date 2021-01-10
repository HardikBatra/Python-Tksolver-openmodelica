model RLCPARALLEL
  Modelica.Electrical.Analog.Basic.Resistor resistor annotation(
    Placement(visible = true, transformation(origin = {5, 5}, extent = {{-19, -19}, {19, 19}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Inductor inductor annotation(
    Placement(visible = true, transformation(origin = {35, 5}, extent = {{-19, -19}, {19, 19}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Capacitor capacitor annotation(
    Placement(visible = true, transformation(origin = {77, 5}, extent = {{-19, -19}, {19, 19}}, rotation = -90)));
  Modelica.Electrical.Analog.Basic.Ground ground annotation(
    Placement(visible = true, transformation(origin = {-68, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Electrical.Analog.Sources.SineVoltage sineVoltage(V = 50, freqHz = 100)  annotation(
    Placement(visible = true, transformation(origin = {-90, 2}, extent = {{-22, -14}, {22, 14}}, rotation = -90)));
  Modelica.Electrical.Analog.Sensors.CurrentSensor currentSensor annotation(
    Placement(visible = true, transformation(origin = {-36, -20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(resistor.p, inductor.p) annotation(
    Line(points = {{5, 24}, {35, 24}}, color = {0, 0, 255}));
  connect(inductor.p, capacitor.p) annotation(
    Line(points = {{35, 24}, {77, 24}}, color = {0, 0, 255}));
  connect(capacitor.n, inductor.n) annotation(
    Line(points = {{77, -14}, {35, -14}}, color = {0, 0, 255}));
  connect(inductor.n, resistor.n) annotation(
    Line(points = {{35, -14}, {5, -14}}, color = {0, 0, 255}));
  connect(sineVoltage.p, resistor.p) annotation(
    Line(points = {{-90, 24}, {5, 24}}, color = {0, 0, 255}));
  connect(sineVoltage.n, ground.p) annotation(
    Line(points = {{-90, -20}, {-68, -20}}, color = {0, 0, 255}));
  connect(ground.p, currentSensor.p) annotation(
    Line(points = {{-68, -20}, {-46, -20}}, color = {0, 0, 255}));
  connect(currentSensor.n, resistor.n) annotation(
    Line(points = {{-26, -20}, {-12.5, -20}, {-12.5, -14}, {5, -14}}, color = {0, 0, 255}));
  annotation(
    uses(Modelica(version = "3.2.3")),
    Diagram(graphics = {Text(origin = {-27, 83}, extent = {{-17, 7}, {75, -9}}, textString = "RLC PARALLEL", textStyle = {TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic, TextStyle.Italic})}));
end RLCPARALLEL;
