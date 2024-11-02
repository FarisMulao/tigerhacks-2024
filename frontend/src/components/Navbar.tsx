import React, { useState } from "react";
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  Avatar,
  IconButton,
  Menu,
  MenuItem,
} from "@mui/material";
import { Link } from "react-router-dom";

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleProfileClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar
      position="static"
      sx={{ bgcolor: "#f7f9fc", color: "#000", boxShadow: 1 }}
    >
      <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>
        <Box display="flex" alignItems="center">
          <Typography
            variant="h6"
            sx={{ fontWeight: "bold", color: "#000", textDecoration: "none" }}
            component={Link}
            to="/"
          >
            PLID
          </Typography>
        </Box>

        <Box display="flex" alignItems="center">
          {isLoggedIn ? (
            <>
              <Button
                component={Link}
                to="/upload"
                sx={{
                  color: "#000",
                  "&:hover": { color: "#1976d2" },
                  fontWeight: "bold",
                  marginRight: 2,
                }}
              >
                Upload
              </Button>
              <Button
                component={Link}
                to="/my-plants"
                sx={{
                  color: "#000",
                  "&:hover": { color: "#1976d2" },
                  fontWeight: "bold",
                  marginRight: 2,
                }}
              >
                My Plants
              </Button>

              <IconButton onClick={handleProfileClick} sx={{ padding: 0 }}>
                <Avatar
                  alt="Profile"
                  src="/path/to/profile-picture.jpg" // Placeholder, replace with actual profile picture source
                  sx={{ width: 36, height: 36 }}
                />
              </IconButton>
              <Menu
                anchorEl={anchorEl}
                open={Boolean(anchorEl)}
                onClose={handleClose}
                anchorOrigin={{
                  vertical: "bottom",
                  horizontal: "right",
                }}
                transformOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
              >
                <MenuItem component={Link} to="/profile" onClick={handleClose}>
                  Profile
                </MenuItem>
                <MenuItem
                  onClick={() => {
                    setIsLoggedIn(false);
                    handleClose();
                  }}
                >
                  Log Out
                </MenuItem>
              </Menu>
            </>
          ) : (
            <>
              <Button
                component={Link}
                to="/signup"
                sx={{
                  color: "#000",
                  "&:hover": { color: "#1976d2" },
                  fontWeight: "bold",
                  marginRight: 2,
                }}
              >
                Sign Up
              </Button>
              <Button
                component={Link}
                to="/login"
                sx={{
                  backgroundColor: "#000",
                  color: "#fff",
                  padding: "6px 16px",
                  borderRadius: "8px",
                  "&:hover": { backgroundColor: "#333" },
                }}
                onClick={() => setIsLoggedIn(true)}
              >
                Log In
              </Button>
            </>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
