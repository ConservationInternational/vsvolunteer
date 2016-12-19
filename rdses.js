var RSVP = require('rsvp');

var elasticsearch = require('elasticsearch');
var esc = new elasticsearch.Client({
	host: 'ec2-54-144-196-39.compute-1.amazonaws.com:9200',
	log: 'error'
});

var pg = require('pg');
var pgc = new pg.Client("postgres://postgres:postgres@cipg.cwmahp7esvi2.us-east-1.rds.amazonaws.com:5432/vitalsigns_staging");

pgc.connect(function (err) {
	if (err) throw err;

	/*
	 curation__eplotsoils_lab
	 curation__household
	 curation__agric_livestock
	 curation__agric_byprod
	 */
	var viewName = 'curation__agric_byprod';
	pgc.query('SELECT uuid AS id, row_to_json(' + viewName + ') AS body FROM ' + viewName, function (err, result) {
		if (err) throw err;

		var promises = result.rows.map(function (row) {
			return new RSVP.Promise(function (resolve, reject) {
				var doc = row.body;
				console.info('es id', row.id);

				if (typeof doc['latitude'] !== 'undefined') {
					doc['location'] = [
						doc['longitude'],
						doc['latitude']
					];
					delete doc['latitude'];
					delete doc['longitude'];
				} else {
					delete doc['location'];
					delete doc['latitude'];
					delete doc['longitude'];
				}

				esc.update({
					index: viewName,
					type: viewName,
					id: row.id,
					body: {
						doc: doc,
						doc_as_upsert: true
					}
				}, function (err, response) {
					if (err)
						return reject(err);

					console.info('es ok', row.id);
					resolve();
				});
			});
		});

		RSVP.all(promises).then(function () {
			console.info('es all ok');

			pgc.end(function (err) {
				if (err) throw err;
			});
		});
	});
});