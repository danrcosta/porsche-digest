#!/bin/bash
# Deploy script - Copy to: /c/Users/SERVER/Hermes-Workspace/porsche-digest/deploy.sh

echo "🚀 Starting Porsche Digest V5 Deploy..."
echo "=================================="

cd /c/Users/SERVER/Hermes-Workspace/porsche-digest || exit 1

echo "📁 Working Directory: $(pwd)"
echo ""

# Check files
echo "📋 Checking required files..."
files=("index-v5.html" "styles-v5.css" "manifest.json" "worker.js")
for f in "${files[@]}"; do
    if [ -f "$f" ]; then
        echo "   ✅ $f"
    else
        echo "   ❌ $f MISSING"
        exit 1
    fi
done

echo ""
echo "🔐 Checking .env..."
if [ -f ".env" ]; then
    echo "   ✅ .env exists"
else
    echo "   ❌ .env missing - please create it"
    exit 1
fi

echo ""
echo "🔧 Deploying to Cloudflare Pages..."
npx wrangler pages deploy . --project-name=porsche-digest --branch main

echo ""
echo "✅ Deploy complete!"
echo "🔗 https://digest.costafamily.ai"