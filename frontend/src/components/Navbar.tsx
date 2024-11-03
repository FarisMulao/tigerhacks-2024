import React, { useState, useEffect } from "react";
import GrassIcon from "@mui/icons-material/Grass";
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

interface Props {
  email?: string;
  name?: string;
}

const Navbar = ({ email, name }: Props) => {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const [loggedIn, setLoggedIn] = useState(Boolean(email && name));

  useEffect(() => {
    setLoggedIn(Boolean(email && name));
  }, [email, name]);

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
          <GrassIcon />
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
          {loggedIn ? (
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
                to="/myplants"
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
                  alt={name}
                  src="/path/to/profile-picture.jpg"
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
                <MenuItem onClick={handleClose}>{name}</MenuItem>
                <MenuItem onClick={handleClose}>{email}</MenuItem>
                <MenuItem
                  onClick={() => {
                    // Handle log out functionality here
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
                onClick={() => (window.location.href = "/signup")}
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
                onClick={() => (window.location.href = "/login")}
                sx={{
                  backgroundColor: "#000",
                  color: "#fff",
                  padding: "6px 16px",
                  borderRadius: "8px",
                  "&:hover": { backgroundColor: "#333" },
                }}
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
