-- =========================================
-- Insert users
-- =========================================
INSERT INTO users (full_name, email, active)
VALUES
('Ana Perez', 'ana.perez@example.com', TRUE),
('Carlos Gomez', 'carlos.gomez@example.com', TRUE),
('Lucia Fernandez', 'lucia.fernandez@example.com', TRUE);

-- =========================================
-- Insert services
-- =========================================
INSERT INTO services (name, description)
VALUES
('GitHub', 'Code repository'),
('ClickUp', 'Task and project management'),
('Digital Ocean', 'Cloud infrastructure provider'),
('Microsoft 365', 'Cloud office suite');

-- =========================================
-- Insert roles
-- =========================================
-- Each role is associated with a service
INSERT INTO roles (service_id, name, description)
VALUES
(1, 'Admin', 'Full access to repositories'),
(1, 'Read-only', 'Read-only access to repositories'),
(2, 'Project Manager', 'Can manage projects and tasks'),
(2, 'Viewer', 'Can only view projects and tasks'),
(3, 'Admin', 'Total control of resources'),
(3, 'User', 'Limited access to resources'),
(4, 'Admin', 'Full administration'),
(4, 'User', 'Standard user');

-- =========================================
-- Insert accesses
-- =========================================
-- Links users with services and roles
INSERT INTO accesses (user_id, service_id, role_id)
VALUES
(1, 1, 1),  -- Ana: Admin on GitHub
(1, 2, 3),  -- Ana: Project Manager on ClickUp
(2, 1, 2),  -- Carlos: Read-only on GitHub
(2, 3, 6),  -- Carlos: User on Digital Ocean
(3, 4, 8);  -- Lucia: User on Microsoft 365
