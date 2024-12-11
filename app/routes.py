from flask import Blueprint, jsonify
from app.models import FinancialData
from datetime import datetime
from sqlalchemy import text
from app import db

bp = Blueprint('main', __name__)

@bp.route('/api/financial-data', methods=['GET'])
def get_financial_data():
    data = FinancialData.query.all()
    return jsonify([entry.to_dict() for entry in data])

@bp.route('/api/summary', methods=['GET'])
def get_summary():
    yearly_summaries = {}
    data = FinancialData.query.all()
    
    for entry in data:
        year = entry.year
        if year not in yearly_summaries:
            yearly_summaries[year] = {
                'total_revenue': 0,
                'total_cost': 0,
                'total_profit': 0,
                'average_profit_margin': 0,
                'data_points': 0
            }
        
        summary = yearly_summaries[year]
        summary['total_revenue'] += entry.revenue
        summary['total_cost'] += entry.cost
        summary['total_profit'] += entry.profit
        summary['average_profit_margin'] += entry.profit_margin
        summary['data_points'] += 1
    
    # Calculate averages
    for year in yearly_summaries:
        summary = yearly_summaries[year]
        summary['average_profit_margin'] = round(
            summary['average_profit_margin'] / summary['data_points'], 2
        )
    
    return jsonify(yearly_summaries)

@bp.route('/api/trends', methods=['GET'])
def get_trends():
    data = FinancialData.query.all()
    yearly_data = {}
    
    # Aggregate data by year
    for entry in data:
        year = entry.year
        if year not in yearly_data:
            yearly_data[year] = {
                'revenue': 0,
                'cost': 0,
                'profit': 0,
                'margins': []
            }
        
        yearly_data[year]['revenue'] += entry.revenue
        yearly_data[year]['cost'] += entry.cost
        yearly_data[year]['profit'] += entry.profit
        yearly_data[year]['margins'].append(entry.profit_margin)
    
    # Calculate trends
    trends = {
        'revenue_growth': [],
        'cost_growth': [],
        'profit_growth': []
    }
    
    years = sorted(yearly_data.keys())
    for i in range(1, len(years)):
        prev_year = yearly_data[years[i-1]]
        curr_year = yearly_data[years[i]]
        
        for metric in ['revenue', 'cost', 'profit']:
            growth = ((curr_year[metric] - prev_year[metric]) / prev_year[metric]) * 100
            trends[f'{metric}_growth'].append({
                'year': years[i],
                'growth': round(growth, 2)
            })
    
    return jsonify(trends)

# Health Check
@bp.route('/health', methods=['GET'])
def health_check():
    health_status = {
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'database': 'connected',
        'api_version': 'v1'
    }
    
    try:
        # Test database connection
        db.session.execute(text('SELECT 1'))
        db.session.commit()
    except Exception as e:
        health_status['status'] = 'unhealthy'
        health_status['database'] = 'disconnected'
        health_status['error'] = str(e)
    
    # Set response status code based on health check results
    status_code = 200 if health_status['status'] == 'healthy' else 503
    
    return jsonify(health_status), status_code