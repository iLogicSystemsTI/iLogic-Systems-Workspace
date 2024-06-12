-- Crear la primera tabla: Empleados
CREATE TABLE Empleados (
    ID INT PRIMARY KEY,
    Nombre NVARCHAR(50),
    Departamento NVARCHAR(50)
);
GO

-- Insertar datos en la tabla Empleados
INSERT INTO 
Empleados (ID, Nombre, Departamento) VALUES
(1, 'Juan', 'Ventas'),
(2, 'María', 'Recursos Humanos'),
(3, 'Pedro', 'Ventas'),
(4, 'Laura', 'Marketing'),
(5, 'Ana', 'Ventas');  -- Empleado sin ventas
GO

-- Crear la segunda tabla: Ventas
CREATE TABLE Ventas (
    ID INT PRIMARY KEY,
    EmpleadoID INT,
    Monto DECIMAL(10, 2),
    Fecha DATE
);
GO

-- Insertar datos en la tabla Ventas
INSERT INTO 
Ventas (ID, EmpleadoID, Monto, Fecha) VALUES
(1, 1, 100.00, '2022-06-01'),
(2, 1, 150.00, '2022-06-02'),
(3, 2, 200.00, '2022-06-03'),
(4, 3, 120.00, '2022-06-04');
GO

-- Ejemplo de Inner Join
-- "Muestra solo los empleados con ventas."
SELECT
	e.Nombre AS NombreEmpleado,
	e.Departamento,
	v.Monto,
	v.Fecha
FROM
	Empleados e
INNER JOIN Ventas v ON
	e.ID = v.EmpleadoID;
GO

-- Ejemplo de Left Join
-- "Muestra todos los empleados, con o sin ventas."
SELECT
	e.Nombre AS NombreEmpleado,
	e.Departamento,
	v.Monto,
	v.Fecha
FROM
	Empleados e
LEFT JOIN Ventas v ON
	e.ID = v.EmpleadoID;
GO

-- Ejemplo de Right Join
-- "Muestra todas las ventas, 
-- incluyendo ventas sin empleados registrados."
SELECT
	e.Nombre AS NombreEmpleado,
	e.Departamento,
	v.Monto,
	v.Fecha
FROM
	Empleados e
RIGHT JOIN Ventas v ON
	e.ID = v.EmpleadoID;
GO

-- Ejemplo de Full Join
-- "Muestra todos los empleados y ventas, 
-- sin importar si tienen coincidencias."
SELECT
	e.Nombre AS NombreEmpleado,
	e.Departamento,
	v.Monto,
	v.Fecha
FROM
	Empleados e
FULL JOIN Ventas v ON
	e.ID = v.EmpleadoID;
GO
