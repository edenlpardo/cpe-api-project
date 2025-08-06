import React, { useState } from 'react';
import { Popover, Typography, Link } from '@mui/material';

const truncate = (text, length = 30) => text.length > length ? text.slice(0, length) + "..." : text;

const ReferencePopover = ({ references }) => {
  const [anchorEl, setAnchorEl] = useState(null);

  if (!references || references.length === 0) return <span>-</span>;

  const firstTwo = references.slice(0, 2);
  const extraCount = references.length - 2;

  const handleClick = (event) => setAnchorEl(event.currentTarget);
  const handleClose = () => setAnchorEl(null);

  return (
    <>
      {firstTwo.map((link, idx) => (
        <Link key={idx} href={link} target="_blank" rel="noopener noreferrer" title={link}>
          {truncate(link)}
        </Link>
      ))}
      {extraCount > 0 && (
        <>
          <Link onClick={handleClick} component="button">+{extraCount} more</Link>
          <Popover open={Boolean(anchorEl)} anchorEl={anchorEl} onClose={handleClose} anchorOrigin={{ vertical: 'bottom', horizontal: 'left' }}>
            <div style={{ padding: '10px', maxWidth: '300px' }}>
              {references.map((link, i) => (
                <Typography key={i} sx={{ mb: 1 }}>
                  <Link href={link} target="_blank" rel="noopener noreferrer" title={link}>
                    {truncate(link)}
                  </Link>
                </Typography>
              ))}
            </div>
          </Popover>
        </>
      )}
    </>
  );
};

export default ReferencePopover;
