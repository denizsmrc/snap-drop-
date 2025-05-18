const functions = require('@google-cloud/functions-framework');

functions.http('fileStats', (req, res) => {
  // Enable CORS
  res.set('Access-Control-Allow-Origin', '*');
  
  if (req.method === 'OPTIONS') {
    res.set('Access-Control-Allow-Methods', 'GET, POST');
    res.set('Access-Control-Allow-Headers', 'Content-Type');
    res.status(204).send('');
    return;
  }

  try {
    const fileData = req.body;
    
    // Calculate file statistics
    const stats = {
      timestamp: new Date().toISOString(),
      fileSize: fileData.size,
      fileType: fileData.type,
      transferSpeed: fileData.transferSpeed || 'N/A',
      transferTime: fileData.transferTime || 'N/A'
    };

    // Log to Cloud Logging
    console.log('File transfer statistics:', stats);

    res.status(200).json(stats);
  } catch (error) {
    console.error('Error processing file stats:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}); 