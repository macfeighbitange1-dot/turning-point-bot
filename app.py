<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turning Point Bot | Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: #1e293b;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            border: 1px solid #334155;
            max-width: 400px;
        }
        .status-badge {
            display: inline-block;
            background: #065f46;
            color: #34d399;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-bottom: 20px;
            text-transform: uppercase;
        }
        h1 { margin: 10px 0; color: #38bdf8; }
        p { color: #94a3b8; line-height: 1.6; }
        .footer { margin-top: 30px; font-size: 0.7rem; color: #475569; }
        .pulse {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #34d399;
            border-radius: 50%;
            margin-right: 5px;
            box-shadow: 0 0 0 rgba(52, 211, 153, 0.4);
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(52, 211, 153, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="status-badge"><span class="pulse"></span> System Live</div>
        <h1>Turning Point Bot</h1>
        <p>The WhatsApp automation engine is running successfully.</p>
        <p>Connected to <strong>Twilio API</strong>.</p>
        <div class="footer">
            Hosted on Render • Powered by Python & Flask
        </div>
    </div>
</body>
</html>
