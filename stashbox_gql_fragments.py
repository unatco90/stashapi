DEVELOP="""
fragment URLFragment on URL {
	url
	site {
		id
		name
		url
	}
}
fragment ImageFragment on Image {
	id
	url
	width
	height
}
fragment StudioFragment on Studio {
	name
	id
	urls {
		...URLFragment
	}
	images {
		...ImageFragment
	}
}
fragment TagFragment on Tag {
	name
	id
}
fragment FuzzyDateFragment on FuzzyDate {
	date
	accuracy
}
fragment MeasurementsFragment on Measurements {
	band_size
	cup_size
	waist
	hip
}
fragment BodyModificationFragment on BodyModification {
	location
	description
}
fragment PerformerFragment on Performer {
	id
	name
	disambiguation
	aliases
	gender
	merged_ids
	urls {
		...URLFragment
	}
	images {
		...ImageFragment
	}
	birthdate {
		...FuzzyDateFragment
	}
	ethnicity
	country
	eye_color
	hair_color
	height
	measurements {
		...MeasurementsFragment
	}
	breast_type
	career_start_year
	career_end_year
	tattoos {
		...BodyModificationFragment
	}
	piercings {
		...BodyModificationFragment
	}
}
fragment PerformerAppearanceFragment on PerformerAppearance {
	as
	performer {
		...PerformerFragment
	}
}
fragment FingerprintFragment on Fingerprint {
	algorithm
	hash
	duration
}
fragment SceneFragment on Scene {
	id
	title
	details
	duration
	date
	urls {
		...URLFragment
	}
	images {
		...ImageFragment
	}
	studio {
		...StudioFragment
	}
	tags {
		...TagFragment
	}
	performers {
		...PerformerAppearanceFragment
	}
	fingerprints {
		...FingerprintFragment
	}
}
fragment SceneEditFragment on Scene {
	title
	date
	duration
	director
	code
	details
	studio { id }
	performers {
		performer { id }
		as
	}
	images { id }
	tags { id }
	urls {
		url
		site { id }
	}
}
fragment EditFragment on Edit {
	applied
	closed
	created
	destructive
	details
	expires
	id
	old_details
	operation
	updated
	user { name }
	vote_count
}
fragment Draft on Draft {
	created
	expires
	id
}
fragment PerformerDraft on PerformerDraft {
	id
	name
	aliases
	gender
	birthdate
	urls
	ethnicity
	country
	eye_color
	hair_color
	height
	measurements
	breast_type
	tattoos
	piercings
	career_start_year
	career_end_year
	image {
		...ImageFragment
		__typename
	}
	__typename
}
fragment SceneDraft on SceneDraft {
	id
	title
	code
	details
	director
	date
	url {
		...URLFragment
		__typename
	}
	studio {
		... on Studio {
		...StudioFragment
		__typename
		}
		... on DraftEntity {
		draftID: id
		name
		__typename
		}
		__typename
	}
	performers {
		... on Performer {
		...PerformerFragment
		__typename
		}
		... on DraftEntity {
		draftID: id
		name
		__typename
		}
		__typename
	}
	tags {
		... on Tag {
		...TagFragment
		__typename
		}
		... on DraftEntity {
		draftID: id
		name
		__typename
		}
		__typename
	}
	fingerprints {
		hash
		algorithm
		duration
		__typename
	}
	image {
		...ImageFragment
		__typename
	}
	__typename
	}
	__typename
	}
	__typename
}
"""